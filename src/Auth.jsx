import { useState, useEffect } from 'react'
import axios from 'axios'

export default function Auth() {
    const [accessToken, setAccessToken] = useState()

    useEffect(() => {
        axios.post('http://127.0.0.1:5000/auth')
            .then(res => {
                setAccessToken(res.data.access_token)
            })
            .catch((error) => {
                console.log(`ERROR: ${error}`)
            })
    })

    return accessToken
}