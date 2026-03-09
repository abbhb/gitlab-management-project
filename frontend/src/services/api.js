import appConfig from '../config'

function getCookie(name) {
  const value = `; ${document.cookie}`
  const parts = value.split(`; ${name}=`)
  if (parts.length === 2) {
    return parts.pop().split(';').shift()
  }
  return ''
}

function buildUrl(path, params) {
  if (!params || Object.keys(params).length === 0) {
    return path
  }

  const search = new URLSearchParams()
  Object.keys(params).forEach((key) => {
    const value = params[key]
    if (value !== undefined && value !== null && value !== '') {
      search.append(key, value)
    }
  })

  const query = search.toString()
  return query ? `${path}?${query}` : path
}

async function request(path, options = {}) {
  const { method = 'GET', data, params, headers = {} } = options
  const response = await fetch(buildUrl(path, params), {
    method,
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json',
      'X-Requested-With': 'XMLHttpRequest',
      'X-CSRFToken': getCookie('csrftoken') || appConfig.csrfToken,
      ...headers
    },
    body: data === undefined ? undefined : JSON.stringify(data)
  })

  const payload = await response.json().catch(() => ({
    result: false,
    message: '服务返回了无法识别的数据'
  }))

  if (!response.ok || payload.result === false) {
    const error = new Error(payload.message || '请求失败')
    error.payload = payload
    error.status = response.status
    throw error
  }

  return payload.data
}

export function get(path, params) {
  return request(path, { params })
}

export function post(path, data) {
  return request(path, { method: 'POST', data })
}

export function put(path, data) {
  return request(path, { method: 'PUT', data })
}

export function del(path) {
  return request(path, { method: 'DELETE' })
}
