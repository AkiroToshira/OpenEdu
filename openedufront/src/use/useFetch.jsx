import {useState, useEffect} from 'react'

const useFetch = (url) => {
  const [data, setData] = useState(null)
  const [isLoading, setIsLoading] = useState(true)
  const authToken = localStorage.getItem('access')
  useEffect(() => {
	const fetchData = async () => {
	  setIsLoading(true)
	  fetch(url, {
		'Authorization': 'JWT' + authToken,
		headers: {
		  'Content-Type': 'application/json'
		}
	  })
		  .then((response) => response.json())
		  .then((result) => {
			setData(result)
			setIsLoading(false)
		  })
	}
	fetchData()
  }, [])
  return [data, isLoading]
}

export default useFetch
