import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom'

export default function HomeRedirect() {
    let navigate = useNavigate();

    useEffect(() => {
        navigate('/home', { replace: true });
    }, [navigate]);

    return null
}