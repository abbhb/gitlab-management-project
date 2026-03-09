const defaults = {
  page: 'dashboard',
  pageProps: {},
  csrfToken: '',
  user: {
    username: '',
    enterprise_username: ''
  },
  urls: {
    home: '/',
    projectList: '/subscription/projects/',
    subscriptionList: '/subscription/my-subscriptions/',
    console: '',
    logout: ''
  }
}

function parseFrontendConfig() {
  const node = document.getElementById('frontend-config')
  if (!node) {
    return defaults
  }

  try {
    return {
      ...defaults,
      ...JSON.parse(node.textContent || '{}')
    }
  } catch (error) {
    console.error('Failed to parse frontend config', error)
    return defaults
  }
}

export default parseFrontendConfig()
