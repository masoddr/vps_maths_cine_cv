export const defaultMeta = {
  title: 'Cinéphoria - Les séances de cinéma à Toulouse',
  description: 'Trouvez facilement toutes les séances de cinéma à Toulouse. Horaires, films à l\'affiche et informations sur les salles de cinéma toulousaines.',
  image: '/images/social-share.jpg',
  url: 'https://cinephoria.fr'
}

export const generateMeta = (options: Partial<typeof defaultMeta> = {}) => {
  const meta = { ...defaultMeta, ...options }

  return [
    { name: 'description', content: meta.description },
    { property: 'og:title', content: meta.title },
    { property: 'og:description', content: meta.description },
    { property: 'og:image', content: meta.image },
    { property: 'og:url', content: meta.url },
    { property: 'og:type', content: 'website' },
    { name: 'twitter:card', content: 'summary_large_image' },
    { name: 'twitter:title', content: meta.title },
    { name: 'twitter:description', content: meta.description },
    { name: 'twitter:image', content: meta.image }
  ]
} 