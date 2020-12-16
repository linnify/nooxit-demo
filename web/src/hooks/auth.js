import { useLocation, useHistory } from "react-router-dom";
import { useEffect, useState } from "react";
import {clearLocalToken, getLocalToken, setLocalToken} from "../helpers/utils";
import {getProfile} from "../services/api";
const queryString = require('query-string');

/**
 * Hook for checking if the current user is authenticated
 * First check if the URL has the token set in the query params
 * If not check if we already have the token in the local storage
 *
 * If the URL has a token in the query param, grab the token and set the user
 */
function useAuth() {
  const [isLoading, setIsLoading] = useState(true);
  const [user, setUser] = useState(null)
  const location = useLocation()
  const history = useHistory()
  
  
  useEffect(() => {
    const parsed = queryString.parse(location.search);
    if (parsed.token) {
      history.replace(location.pathname, {
        search: '',
      })
      setLocalToken(parsed.token)
    }
    const currentToken = getLocalToken()
    if (!currentToken) {
      // User not authenticated
      setIsLoading(false);
      return;
    }
    
    loadUserProfile()
  }, [])
  
  /**
   * Load the user profile
   * If there is an error logout the user
   * @return {Promise<void>}
   */
  async function loadUserProfile() {
    try {
      const profile = await getProfile()
      setUser(profile)
    } catch (e) {
      logout()
    } finally {
      setIsLoading(false);
    }
  }
  
  function logout() {
    clearLocalToken()
    setUser(null)
  }
  
  return [user, isLoading, logout]
}

export default useAuth
