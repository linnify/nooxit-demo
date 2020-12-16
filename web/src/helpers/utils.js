const LOCAL_STORAGE_TOKEN = 'auth-token'

export function clearLocalToken() {
  localStorage.removeItem(LOCAL_STORAGE_TOKEN)
}

export function setLocalToken(token) {
  localStorage.setItem(LOCAL_STORAGE_TOKEN, token)
}

export function getLocalToken() {
  return localStorage.getItem(LOCAL_STORAGE_TOKEN)
}

export function getAuthHeader() {
  const token = getLocalToken();
  return {
    'Authorization': `${token}`
  }
}
