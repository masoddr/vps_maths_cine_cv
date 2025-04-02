<template>
  <div class="pdf-viewer" :class="{ 'fullscreen': isFullscreen }">
    <!-- Barre d'outils -->
    <div class="bg-white border-b border-gray-200 px-4 py-2 flex items-center justify-between">
      <div class="flex items-center space-x-4">
        <!-- Contrôles de zoom -->
        <div class="zoom-controls flex items-center space-x-2">
          <button
            @click="zoomOut"
            class="p-1 rounded-md hover:bg-gray-100"
            :disabled="scale <= minScale"
          >
            <svg class="h-5 w-5 text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4" />
            </svg>
          </button>
          
          <span class="text-sm text-gray-600">{{ Math.round(scale * 100) }}%</span>
          
          <button
            @click="zoomIn"
            class="p-1 rounded-md hover:bg-gray-100"
            :disabled="scale >= maxScale"
          >
            <svg class="h-5 w-5 text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
            </svg>
          </button>
        </div>

        <!-- Contrôle de page -->
        <div class="page-controls flex items-center space-x-2">
          <button
            @click="previousPage"
            class="p-1 rounded-md hover:bg-gray-100"
            :disabled="currentPage <= 1"
          >
            <svg class="h-5 w-5 text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
            </svg>
          </button>
          
          <span class="text-sm text-gray-600">
            Page {{ currentPage }} sur {{ totalPages }}
          </span>
          
          <button
            @click="nextPage"
            class="p-1 rounded-md hover:bg-gray-100"
            :disabled="currentPage >= totalPages"
          >
            <svg class="h-5 w-5 text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
            </svg>
          </button>
        </div>
      </div>

      <div class="flex items-center space-x-2">
        <!-- Bouton plein écran -->
        <button
          @click="toggleFullscreen"
          class="p-1 rounded-md hover:bg-gray-100"
        >
          <svg v-if="!isFullscreen" class="h-5 w-5 text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4" />
          </svg>
          <svg v-else class="h-5 w-5 text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4h16v16H4z" />
          </svg>
        </button>

        <!-- Bouton fermer -->
        <button
          @click="$emit('close')"
          class="p-1 rounded-md hover:bg-gray-100"
        >
          <svg class="h-5 w-5 text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
    </div>

    <!-- Conteneur du PDF -->
    <div 
      ref="pdfContainer"
      class="pdf-container overflow-auto bg-gray-100 relative"
      @wheel="handleWheel"
      @mousedown="startPan"
      @mousemove="pan"
      @mouseup="stopPan"
      @mouseleave="stopPan"
    >
      <canvas
        ref="pdfCanvas"
        :style="{
          transform: `scale(${scale}) translate(${panX}px, ${panY}px)`,
          transformOrigin: '0 0'
        }"
      ></canvas>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import * as pdfjsLib from 'pdfjs-dist'

// Props
const props = defineProps({
  pdfUrl: {
    type: String,
    required: true
  }
})

// Emits
defineEmits(['close'])

// Refs
const pdfContainer = ref(null)
const pdfCanvas = ref(null)
const scale = ref(1)
const currentPage = ref(1)
const totalPages = ref(1)
const isFullscreen = ref(false)
const panX = ref(0)
const panY = ref(0)
const isPanning = ref(false)
const lastX = ref(0)
const lastY = ref(0)

// Constants
const minScale = 0.5
const maxScale = 3
const scaleStep = 0.1

// PDF rendering
let pdfDoc = null
let pdfPage = null

onMounted(async () => {
  try {
    // Charger le PDF
    pdfDoc = await pdfjsLib.getDocument(props.pdfUrl).promise
    totalPages.value = pdfDoc.numPages
    renderPage()
  } catch (error) {
    console.error('Erreur lors du chargement du PDF:', error)
  }
})

// Fonctions de zoom
function zoomIn() {
  if (scale.value < maxScale) {
    scale.value = Math.min(scale.value + scaleStep, maxScale)
    renderPage()
  }
}

function zoomOut() {
  if (scale.value > minScale) {
    scale.value = Math.max(scale.value - scaleStep, minScale)
    renderPage()
  }
}

function handleWheel(e) {
  if (e.ctrlKey) {
    e.preventDefault()
    if (e.deltaY < 0) {
      zoomIn()
    } else {
      zoomOut()
    }
  }
}

// Fonctions de navigation
async function renderPage() {
  if (!pdfDoc) return

  try {
    pdfPage = await pdfDoc.getPage(currentPage.value)
    const viewport = pdfPage.getViewport({ scale: scale.value })

    const canvas = pdfCanvas.value
    const context = canvas.getContext('2d')

    canvas.height = viewport.height
    canvas.width = viewport.width

    await pdfPage.render({
      canvasContext: context,
      viewport: viewport
    }).promise
  } catch (error) {
    console.error('Erreur lors du rendu de la page:', error)
  }
}

async function nextPage() {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
    await renderPage()
  }
}

async function previousPage() {
  if (currentPage.value > 1) {
    currentPage.value--
    await renderPage()
  }
}

// Fonctions de déplacement
function startPan(e) {
  isPanning.value = true
  lastX.value = e.clientX
  lastY.value = e.clientY
}

function pan(e) {
  if (!isPanning.value) return

  const deltaX = e.clientX - lastX.value
  const deltaY = e.clientY - lastY.value

  panX.value += deltaX / scale.value
  panY.value += deltaY / scale.value

  lastX.value = e.clientX
  lastY.value = e.clientY
}

function stopPan() {
  isPanning.value = false
}

// Plein écran
function toggleFullscreen() {
  isFullscreen.value = !isFullscreen.value
  if (isFullscreen.value) {
    if (document.documentElement.requestFullscreen) {
      document.documentElement.requestFullscreen()
    }
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen()
    }
  }
}

// Observer les changements
watch([scale, currentPage], () => {
  renderPage()
})
</script>

<style scoped>
.pdf-viewer {
  @apply fixed inset-0 z-50 flex flex-col bg-white;
}

.pdf-container {
  @apply flex-1;
  height: calc(100vh - 3rem);
}

.fullscreen {
  @apply fixed inset-0 z-50;
}

/* Styles pour le mode mobile */
@media (max-width: 640px) {
  .pdf-viewer {
    @apply touch-pan-y;
  }
  
  .zoom-controls {
    @apply hidden;
  }
}
</style> 