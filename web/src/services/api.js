import {getAuthHeader} from "../helpers/utils";
import {API_HOST} from "../helpers/constants";
const axios = require('axios')

export async function getProfile() {
  const url = `${API_HOST}/auth/profile`
  const response = await axios.get(url, { headers: getAuthHeader() })
  return response.data
}

export async function getMembers() {
  const url = `${API_HOST}/members`
  try {
    const response = await axios.get(url, {headers: getAuthHeader()})
    return response.data
  } catch (e) {
    const message = e.response.data?.detail;
    throw new Error(message)
  }
}

export async function getUsers() {
  const url = `${API_HOST}/users`
  try {
    const response = await axios.get(url, {headers: getAuthHeader()})
    return response.data
  } catch (e) {
    const message = e.response.data?.detail;
    throw new Error(message)
  }
  
}
