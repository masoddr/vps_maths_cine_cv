import { defineStore } from 'pinia'

// Définir un type pour les cinémas connus
type CinemaName = 'ABC' | 'UGC Montaudran' | 'American Cosmograph' | 'Le cratère' | 'Pathé Wilson' | 'Utopia Borderouge'

interface Cinema {
  id: string
  nom: string
  adresse: string
  ville: string
  nombreSalles: number
  telephone: string
  siteWeb: string
  latitude: number
  longitude: number
}

const CINEMA_COLORS: Record<CinemaName, string> = {
  'ABC': 'rgb(59, 130, 246)', // blue-500
  'UGC Montaudran': 'rgb(220, 38, 38)', // red-600
  'American Cosmograph': 'rgb(220, 38, 38)', // red-600
  'Le cratère': 'rgb(220, 38, 38)', // red-600
  'Pathé Wilson': 'rgb(220, 38, 38)', // red-600
  'Utopia Borderouge': 'rgb(220, 38, 38)', // red-600
}

const CINEMAS: Cinema[] = [
  {
    id: 'ABC',
    nom: 'ABC',
    adresse: '13 Rue Saint-Bernard',
    ville: 'Toulouse',
    nombreSalles: 3,
    telephone: '05 61 21 20 46',
    siteWeb: 'https://abc-toulouse.fr',
    latitude: 43.60274,
    longitude: 1.44671
  },
  {
    id: 'AMERICAN_COSMOGRAPH',
    nom: 'American Cosmograph',
    adresse: '24 Rue Montardy',
    ville: 'Toulouse',
    nombreSalles: 3,
    telephone: '05 61 21 22 11',
    siteWeb: 'https://www.american-cosmograph.fr',
    latitude: 43.60398,
    longitude: 1.44461
  },
  {
    id: 'UTOPIA_BORDEROUGE',
    nom: 'Utopia Borderouge',
    adresse: '59 Avenue Maurice Bourges-Maunoury',
    ville: 'Toulouse',
    nombreSalles: 3,
    telephone: '05 61 50 50 43',
    siteWeb: 'http://www.cinemas-utopia.org/toulouse',
    latitude: 43.63961,
    longitude: 1.45634
  },
  {
    id: 'CRATERE',
    nom: 'Le cratère',
    adresse: '95 Grande Rue Saint-Michel',
    ville: 'Toulouse',
    nombreSalles: 1,
    telephone: '05 61 53 50 53',
    siteWeb: 'https://www.cinemalecratere.com',
    latitude: 43.58574,
    longitude: 1.44561
  },
  {
    id: 'PATHE_WILSON',
    nom: 'Pathé Wilson',
    adresse: '3 Place du Président Thomas Wilson',
    ville: 'Toulouse',
    nombreSalles: 8,
    telephone: '08 92 69 66 96',
    siteWeb: 'https://www.pathe.fr/cinemas/cinema-pathe-wilson',
    latitude: 43.60431,
    longitude: 1.44854
  },
  {
    id: 'UGC_MONTAUDRAN',
    nom: 'UGC Montaudran',
    adresse: '10 Avenue Didier Daurat',
    ville: 'Toulouse',
    nombreSalles: 7,
    telephone: '05 61 00 85 50',
    siteWeb: 'https://www.ugc.fr/cinema-ugc-montaudran.html',
    latitude: 43.57501,
    longitude: 1.48127
  }
]

export const useCinemasStore = defineStore('cinemas', {
  state: () => ({
    colors: CINEMA_COLORS,
    cinemas: CINEMAS
  }),

  getters: {
    getColor: () => {
      return (_cinema: string) => 'rgb(75, 85, 99)' // gray-600 par défaut pour tous
    },
    
    getLightColor: () => {
      return (_cinema: string) => 'rgb(243, 244, 246)' // gray-100 par défaut pour tous
    }
  }
}) 