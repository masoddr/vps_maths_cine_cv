import { defineStore } from 'pinia'

interface Seance {
  titre: string
  heure: string
  jour: string
  cinema: string
  version: string
  duree: number
  tags: string[]
  poster: string
  tmdb_id: number
  date_sortie: string
  note: number
  trailer_url: string | null
  synopsis: string
}

interface SeancesData {
  last_update: string
  seances: Seance[]
}

export const useSeancesStore = defineStore('seances', {
  state: () => ({
    seances: [] as Seance[],
    lastUpdate: '',
    loading: true,
    error: null as string | null
  }),

  getters: {
    // Obtenir les séances par jour
    seancesByDay: (state) => {
      const grouped = {} as Record<string, Seance[]>
      state.seances.forEach(seance => {
        const day = seance.jour.split('T')[0]
        if (!grouped[day]) {
          grouped[day] = []
        }
        grouped[day].push(seance)
      })
      return grouped
    },

    // Obtenir les cinémas uniques
    cinemas: (state) => {
      return [...new Set(state.seances.map(s => s.cinema))]
    },

    // Obtenir les films uniques
    films: (state) => {
      const uniqueFilms = new Map()
      state.seances.forEach(s => {
        if (!uniqueFilms.has(s.tmdb_id)) {
          uniqueFilms.set(s.tmdb_id, s)
        }
      })
      return Array.from(uniqueFilms.values())
    }
  },

  actions: {
    async fetchSeances() {
      try {
        const response = await fetch('/seances.json')
        const data = await response.json() as SeancesData
        this.seances = data.seances
        this.lastUpdate = data.last_update
        this.loading = false
      } catch (e) {
        this.error = e instanceof Error ? e.message : 'Erreur inconnue'
        this.loading = false
      }
    }
  }
}) 