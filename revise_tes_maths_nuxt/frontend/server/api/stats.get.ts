export default defineEventHandler(async (event) => {
  try {
    const config = useRuntimeConfig()
    const response = await fetch(`${config.public.apiBase}/api/stats`)
    const data = await response.json()
    return data
  } catch (error) {
    console.error('Error fetching stats:', error)
    throw createError({
      statusCode: 500,
      message: 'Error fetching stats'
    })
  }
}) 