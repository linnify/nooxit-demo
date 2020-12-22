const LOCAL_STORAGE_TOKEN = 'auth-token'
const LOCAL_STORAGE_ID_TOKEN = 'id-token'

export function setIdToken(idToken) {
  localStorage.setItem(LOCAL_STORAGE_ID_TOKEN, idToken)
}

export function getIdToken() {
  return localStorage.getItem(LOCAL_STORAGE_ID_TOKEN)
}

export function clearLocalToken() {
  localStorage.clear()
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
