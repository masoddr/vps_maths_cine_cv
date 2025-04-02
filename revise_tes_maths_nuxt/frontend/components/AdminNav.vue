  <NuxtLink
    to="/admin/users"
    class="text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-dark-700 hover:text-gray-900 dark:hover:text-gray-100 group flex items-center px-2 py-2 text-sm font-medium rounded-md"
    :class="{ 'bg-gray-100 dark:bg-dark-800 text-gray-900 dark:text-gray-100': $route.path === '/admin/users' }"
  >
    <svg class="text-gray-400 dark:text-gray-500 group-hover:text-gray-500 dark:group-hover:text-gray-400 mr-3 flex-shrink-0 h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
    </svg>
    Utilisateurs
  </NuxtLink>

  <NuxtLink
    to="/admin/messages"
    class="text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-dark-700 hover:text-gray-900 dark:hover:text-gray-100 group flex items-center px-2 py-2 text-sm font-medium rounded-md"
    :class="{ 'bg-gray-100 dark:bg-dark-800 text-gray-900 dark:text-gray-100': $route.path === '/admin/messages' }"
  >
    <svg class="text-gray-400 dark:text-gray-500 group-hover:text-gray-500 dark:group-hover:text-gray-400 mr-3 flex-shrink-0 h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
    </svg>
    Messages
  </NuxtLink> 