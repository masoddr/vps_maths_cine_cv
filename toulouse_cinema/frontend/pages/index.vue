<template>
  <main class="hero">
    <div class="hero-overlay">
      <div class="content-wrapper">
        <div class="hero-content">
          <h1 class="fade-in">
            Cinéma à Toulouse
            <span class="accent">Toutes les séances en un clic</span>
          </h1>
          <p class="subtitle fade-in-delay">
            Explorez toute la programmation des salles toulousaines en un seul endroit. 
            Des blockbusters aux films d'auteur, trouvez votre prochaine séance.
          </p>
          <NuxtLink to="/films" class="cta-button fade-in-delay-2">
            <span>Voir les séances</span>
            <svg class="arrow" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M5 12H19M19 12L12 5M19 12L12 19" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </NuxtLink>
        </div>
      </div>
    </div>
  </main>
  <div class="container mx-auto px-4">
    <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-3 sm:gap-4">
      <div v-for="movie in movies" :key="movie.id" class="flex flex-col">
        <NuxtLink :to="`/films/${movie.id}`" class="movie-card">
          <div class="relative aspect-[2/3] w-full">
            <img
              :src="movie.poster_path"
              :alt="movie.title"
              class="rounded-lg object-cover w-full h-full"
            />
          </div>
          <h3 class="mt-2 text-sm sm:text-base font-medium line-clamp-2">{{ movie.title }}</h3>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { generateMeta } from '~/utils/seo'

onMounted(() => {
  // Effet parallaxe au défilement
  const handleScroll = () => {
    const scrolled = window.pageYOffset;
    const hero = document.querySelector('.hero');
    if (hero) {
      (hero as HTMLElement).style.backgroundPositionY = `${scrolled * 0.5}px`;
    }
  };

  window.addEventListener('scroll', handleScroll);

  // Nettoyage de l'event listener
  onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll);
  });
});

useHead({
  title: 'Cinéma Toulouse - Toutes les séances et films à l\'affiche | Cinéphoria',
  meta: generateMeta({
    title: 'Cinéma Toulouse - Toutes les séances et films à l\'affiche | Cinéphoria',
    description: 'Trouvez toutes les séances de cinéma à Toulouse : films à l\'affiche, horaires des séances, cinémas toulousains. Le guide complet du cinéma à Toulouse.',
    url: 'https://cinephoria.fr'
  }),
  script: [
    {
      type: 'application/ld+json',
      children: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'Organization',
        name: 'Cinéphoria Toulouse',
        url: 'https://cinephoria.fr',
        description: 'Guide des cinémas et séances de films à Toulouse',
        address: {
          '@type': 'PostalAddress',
          addressLocality: 'Toulouse',
          addressRegion: 'Occitanie',
          addressCountry: 'FR'
        },
        areaServed: {
          '@type': 'City',
          name: 'Toulouse'
        }
      })
    }
  ]
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Inter:wght@300;400&display=swap');

.hero {
  height: 100vh;
  width: 100%;
  position: relative;
  background-image: url('/images/cinema-hero.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  overflow: hidden;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to right,
    rgba(0, 0, 0, 0.85) 0%,
    rgba(0, 0, 0, 0.6) 50%,
    rgba(0, 0, 0, 0.4) 100%
  );
  backdrop-filter: blur(1px);
}

.content-wrapper {
  height: 100%;
  max-width: 1440px;
  margin: 0 auto;
  padding: 0 5rem;
  display: flex;
  align-items: center;
}

.hero-content {
  width: 40%;
  min-width: 500px;
}

h1 {
  font-family: 'Playfair Display', serif;
  font-size: clamp(2.5rem, 4vw, 3.5rem);
  color: white;
  line-height: 1.2;
  margin-bottom: 1.5rem;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.accent {
  display: block;
  color: #E4D9FF;
  font-weight: 600;
}

.subtitle {
  font-family: 'Inter', sans-serif;
  font-size: clamp(1rem, 1.2vw, 1.2rem);
  color: rgba(255, 255, 255, 0.9);
  line-height: 1.8;
  margin-bottom: 2.5rem;
  font-weight: 300;
}

.cta-button {
  display: inline-flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 2rem;
  color: white;
  text-decoration: none;
  font-family: 'Inter', sans-serif;
  font-size: 1.1rem;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 4px;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.1);
}

.cta-button:hover {
  background: rgba(255, 255, 255, 0.2);
  border-color: rgba(255, 255, 255, 0.5);
  transform: translateY(-2px);
}

.arrow {
  width: 24px;
  height: 24px;
  transition: transform 0.3s ease;
}

.cta-button:hover .arrow {
  transform: translateX(5px);
}

/* Animations */
.fade-in {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeIn 0.8s ease forwards;
}

.fade-in-delay {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeIn 0.8s ease forwards 0.3s;
}

.fade-in-delay-2 {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeIn 0.8s ease forwards 0.6s;
}

@keyframes fadeIn {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Responsive */
@media (max-width: 1024px) {
  .content-wrapper {
    padding: 0 3rem;
  }
  
  .hero-content {
    width: 60%;
    min-width: auto;
  }
}

@media (max-width: 768px) {
  .content-wrapper {
    padding: 0 1.5rem;
  }
  
  .hero-content {
    width: 100%;
    padding: 0 1rem;
  }
  
  h1 {
    font-size: 2.5rem;
  }
  
  .subtitle {
    font-size: 1rem;
  }
  
  .cta-button {
    width: calc(100% - 2rem);
    justify-content: center;
    padding: 0.875rem 1.5rem;
    font-size: 1rem;
    margin: 0 auto;
  }

  .arrow {
    width: 20px;
    height: 20px;
  }
}

@media (max-width: 360px) {
  .content-wrapper {
    padding: 0 1rem;
  }
  
  .hero-content {
    padding: 0 0.5rem;
  }
  
  .cta-button {
    padding: 0.75rem 1rem;
    font-size: 0.9rem;
  }
}
</style> 