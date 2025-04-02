import { defineNuxtPlugin } from '#app'
import { markRaw } from 'vue'
import 'leaflet/dist/leaflet.css'

// Déclaration pour éviter les erreurs TypeScript
declare module '#app' {
  interface NuxtApp {
    $leaflet: {
      isLoaded: boolean
    }
  }
}

export default defineNuxtPlugin(async (nuxtApp) => {
  // Ne charger qu'une seule fois
  if (process.client && !nuxtApp.$leaflet?.isLoaded) {
    const L = await import('leaflet')
    const { LMap, LTileLayer, LMarker, LPopup } = await import('@vue-leaflet/vue-leaflet')

    // Configuration des icônes
    delete L.Icon.Default.prototype._getIconUrl
    L.Icon.Default.mergeOptions({
      iconUrl: '/marker-icon.png',
      iconRetinaUrl: '/marker-icon-2x.png',
      shadowUrl: '/marker-shadow.png',
    })

    // Enregistrer les composants
    nuxtApp.vueApp.component('LMap', markRaw(LMap))
    nuxtApp.vueApp.component('LTileLayer', markRaw(LTileLayer))
    nuxtApp.vueApp.component('LMarker', markRaw(LMarker))
    nuxtApp.vueApp.component('LPopup', markRaw(LPopup))

    // Marquer comme chargé
    nuxtApp.$leaflet = {
      isLoaded: true
    }
  }
}) 