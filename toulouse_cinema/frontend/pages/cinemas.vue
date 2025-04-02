<template>
  <div class="container mx-auto px-4 py-8">
    <NuxtLink 
      to="/" 
      class="inline-flex items-center text-gray-600 hover:text-gray-800 mb-4"
    >
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z" clip-rule="evenodd" />
      </svg>
      Retour à l'accueil
    </NuxtLink>

    <h1 class="text-3xl font-bold mb-6">Nos Cinémas</h1>

    <!-- Conteneur de la carte -->
    <div class="map-container">
      <ClientOnly>
        <l-map :zoom="13" :center="[43.604, 1.444]">
          <l-tile-layer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution="&copy; OpenStreetMap contributors"
          />
          <l-marker
            v-for="cinema in cinemas"
            :key="cinema.id"
            :lat-lng="[cinema.latitude, cinema.longitude]"
          >
            <l-popup>{{ cinema.nom }}</l-popup>
          </l-marker>
        </l-map>
      </ClientOnly>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="cinema in cinemas" :key="cinema.id" class="bg-white rounded-lg shadow-md p-6">
        <h2 class="text-xl font-semibold mb-2">{{ cinema.nom }}</h2>
        <p class="text-gray-600 mb-2">{{ cinema.adresse }}</p>
        <p class="text-gray-600 mb-4">{{ cinema.ville }}</p>
        <div class="flex items-center space-x-2 mb-3">
          <span class="text-sm text-gray-500">{{ cinema.nombreSalles }} salles</span>
          <span class="text-sm text-gray-500">•</span>
          <span class="text-sm text-gray-500">{{ cinema.telephone }}</span>
        </div>
        
        <!-- Liens -->
        <div class="flex flex-col gap-2">
          <a 
            :href="cinema.siteWeb" 
            target="_blank" 
            rel="noopener noreferrer" 
            class="text-blue-600 hover:text-blue-800 text-sm inline-flex items-center"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" viewBox="0 0 20 20" fill="currentColor">
              <path d="M11 3a1 1 0 100 2h2.586l-6.293 6.293a1 1 0 101.414 1.414L15 6.414V9a1 1 0 102 0V4a1 1 0 00-1-1h-5z" />
              <path d="M5 5a2 2 0 00-2 2v8a2 2 0 002 2h8a2 2 0 002-2v-3a1 1 0 10-2 0v3H5V7h3a1 1 0 000-2H5z" />
            </svg>
            Site web
          </a>
          
          <a 
            :href="getGoogleMapsUrl(cinema)"
            target="_blank" 
            rel="noopener noreferrer" 
            class="text-green-600 hover:text-green-800 text-sm inline-flex items-center"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" />
            </svg>
            Itinéraire Google Maps
          </a>

          <button 
            @click="openTarifsModal(cinema.id)"
            class="text-blue-600 hover:text-blue-800 text-sm inline-flex items-center"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 2a4 4 0 00-4 4v1H5a1 1 0 00-.994.89l-1 9A1 1 0 004 18h12a1 1 0 00.994-1.11l-1-9A1 1 0 0015 7h-1V6a4 4 0 00-4-4zm2 5V6a2 2 0 10-4 0v1h4zm-6 3a1 1 0 112 0 1 1 0 01-2 0zm7-1a1 1 0 100 2 1 1 0 000-2z" clip-rule="evenodd" />
            </svg>
            Voir les tarifs
          </button>
        </div>

        <!-- Modal des tarifs -->
        <div :id="`modal-${cinema.id}`" class="modal" @click="closeTarifsModal(cinema.id)">
          <div class="modal-container" @click.stop>
            <button class="modal-close-button" @click="closeTarifsModal(cinema.id)">×</button>
            <h3 class="modal-title">Tarifs</h3>
            <div class="modal-content">
              <div v-if="getTarifs(cinema.id)">
                <!-- Tarif normal -->
                <p v-if="getTarifs(cinema.id).normal">
                  <strong>Tarif normal : </strong>
                  {{ getTarifs(cinema.id).normal }}€
                </p>

                <!-- Carnet -->
                <div v-if="getTarifs(cinema.id).carnet" class="tarif-section">
                  <p>
                    <strong>Carnet : </strong>
                    {{ getTarifs(cinema.id).carnet.prix }}€ 
                    ({{ getTarifs(cinema.id).carnet.nombre_places }} places)
                    <br>
                    <em>{{ getTarifs(cinema.id).carnet.description }}</em>
                  </p>
                </div>

                <!-- Tarif réduit -->
                <div v-if="getTarifs(cinema.id).reduit" class="tarif-section">
                  <p>
                    <strong>Tarif réduit : </strong>
                    {{ getTarifs(cinema.id).reduit.prix }}€
                  </p>
                  <p v-if="getTarifs(cinema.id).reduit.conditions">
                    <em>Conditions :</em>
                    <ul>
                      <li v-for="condition in getTarifs(cinema.id).reduit.conditions" 
                          :key="condition">
                        {{ condition }}
                      </li>
                    </ul>
                  </p>
                </div>

                <!-- Autres tarifs -->
                <p v-for="(value, key) in getAutresTarifs(cinema.id)" 
                   :key="key" 
                   class="tarif-section">
                  <strong>{{ formatTarifName(key) }} : </strong>
                  {{ value }}€
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <ScrollToTop />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useCinemasStore } from '~/stores/cinemas'
import ScrollToTop from '~/components/ScrollToTop.vue'
import { TARIFS_CINEMA } from '~/constants/tarifs'

const cinemasStore = useCinemasStore()
const cinemas = computed(() => cinemasStore.cinemas)

// Fonction pour générer l'URL Google Maps
function getGoogleMapsUrl(cinema: any) {
  const address = encodeURIComponent(`${cinema.nom}, ${cinema.adresse}, ${cinema.ville}`)
  return `https://www.google.com/maps/dir/?api=1&destination=${address}`
}

function getTarifs(cinemaId) {
  return TARIFS_CINEMA[cinemaId]
}

function getAutresTarifs(cinemaId) {
  const tarifs = TARIFS_CINEMA[cinemaId]
  const autresTarifs = {}
  for (const [key, value] of Object.entries(tarifs)) {
    if (!['normal', 'carnet', 'reduit'].includes(key) && typeof value === 'number') {
      autresTarifs[key] = value
    }
  }
  return autresTarifs
}

function formatTarifName(key) {
  return key.replace(/_/g, ' ').replace(/\w\S*/g, 
    txt => txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase()
  )
}

function openTarifsModal(cinemaId) {
  document.getElementById(`modal-${cinemaId}`).style.display = 'block'
}

function closeTarifsModal(cinemaId) {
  document.getElementById(`modal-${cinemaId}`).style.display = 'none'
}
</script>

<style>
.map-container {
  height: 500px;
  width: 100%;
  margin: 20px 0;
  position: relative;
  z-index: 1;
}

.leaflet-container {
  height: 100%;
  width: 100%;
}

.cinema-buttons {
  display: flex;
  gap: 10px;
  margin-top: 10px;
}

.website-button,
.tarifs-button {
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  text-decoration: none;
  text-align: center;
  flex: 1;
}

.website-button {
  background-color: #28a745;
  color: white;
  border: none;
}

.tarifs-button {
  background-color: #007bff;
  color: white;
  border: none;
}

.website-button:hover {
  background-color: #218838;
}

.tarifs-button:hover {
  background-color: #0056b3;
}

.tarif-section {
  margin-bottom: 15px;
}

.modal {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1000;
}

.modal-container {
  position: relative;
  background-color: white;
  margin: 10% auto;
  padding: 20px;
  width: 80%;
  max-width: 600px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.modal-close-button {
  position: absolute;
  right: 10px;
  top: 10px;
  border: none;
  background: none;
  font-size: 24px;
  cursor: pointer;
  padding: 5px 10px;
}

.modal-title {
  margin-top: 0;
  margin-bottom: 20px;
  text-align: center;
}

.modal-content {
  max-height: 70vh;
  overflow-y: auto;
}

.tarif-section {
  margin-bottom: 15px;
}

:deep(.leaflet-pane),
:deep(.leaflet-control) {
  z-index: 1 !important;
}

:deep(.leaflet-top),
:deep(.leaflet-bottom) {
  z-index: 1 !important;
}
</style> 