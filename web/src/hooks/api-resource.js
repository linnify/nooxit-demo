import {useEffect, useState} from "react";

/**
 * Hook used for fetching a resource from the backend
 * @param getResource an API service function
 * @return the resources and an error message
 */
export function useApiResource(getResource, hasPermission) {
  const [resources, setResources] = useState([]);
  const [error, setError] = useState('')
  
  useEffect(() => {
    if (!hasPermission) {
      setError("Yo don't have permission")
      return
    }
    getResource()
      .then(results => setResources(results))
      .catch(error => setError(error.message))
  }, [])
  
  return [resources, error]
}
