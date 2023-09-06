import url from '../api.json'
import { Link } from 'react-router-dom';
import { useState, useEffect } from 'react';
import ProjectsTable from '../components/TripsTable';

export default function Homepage() {
    const [greeting, setGreeting] = useState([]);
    const [trips, setTrips] = useState([]);
    const token = localStorage.getItem('token');
    
    const loadUser = async () => {
        // Get User
        fetch(url['url'] + '/users/read-one', {
            method: 'GET',
            headers: {
                Authorization: `Bearer ${token}`
            }
        })
            .then((response) => response.json())
            .then((data) => {
                const user = data;
                setUser(user);
                let greeting = "";
                if (user != undefined) {
                    greeting = ", " + user.first_name;
                }
                setGreeting(greeting);
                loadTrips();
            })
            .catch((error) => {
                console.error("Error during loading: ", error);
            });
    }

    const loadTrips = async () => {
        fetch(url['url'] + `/trips/mytrips`, {
            method: 'GET',
            headers: {
                Authorization: `Bearer ${token}`
            }
        })
            .then((response) => response.json())
            .then((data) => {
                const trips = data;
                console.log(trips)
                setTrips(trips);
            })
            .catch((error) => {
                console.error("Error during loading: ", error);
            });
    }

    useEffect(() => {
        loadUser();
    }, []);

    return (
        <div>
            <h1>Project Manager</h1>
            <h2>Welcome{greeting}</h2>
            <button onClick={handleCreateTrip}>Create Project</button>
            <ProjectsTable trips={trips} removeTrip={removeTrip}/>
        </div>
  )
}