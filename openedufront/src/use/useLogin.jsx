import {useEffect, useState} from "react";

const useLogin = (password, username) => {
  const [data, setData] = useState(null)
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
	const fetchData = async () => {
	  setIsLoading(true)
	  fetch("http://127.0.0.1:8000/token/", {
		headers: {
		  'Content-Type': 'application/json'
		}, 'method': "POST",
		body: JSON.stringify({username, password})
	  })
		  .then((response) => response.json())
		  .then((result) => {
			setData(result)
			setIsLoading(false)
		  })
	}
	fetchData()
  }, [])
  if(data) localStorage.setItem('access', data.access)

  return {data, isLoading}
}

export default useLogin