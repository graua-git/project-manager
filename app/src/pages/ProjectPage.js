import url from '../api.json'
import { useParams } from 'react-router-dom';
import { useState, useEffect } from 'react';

export default function ProjectPage() {
    const { id } = useParams();
    const [project, setProject] = useState([]);
    const token = localStorage.getItem('token');

    const loadProject = async () => { 
        fetch(url['url'] + `/projects/read-one/${id}`, {
            method: 'GET',
            headers: {
                Authorization: `Bearer ${token}`
            }
        })
            .then((response) => response.json())
            .then((data) => {
                console.log(data)
                const project = data;
                setProject(project);
            })
            .catch((error) => {
                console.error("Error during loading: ", error);
            });
    }

    const loadTasks = async () => {
        // Get Tasks
        fetch(url['url'] + '/users/read-one', {
            method: 'GET',
            headers: {
                Authorization: `Bearer ${token}`
            }
        })
            .then((response) => response.json())
            .then((data) => {
                
            })
            .catch((error) => {
                console.error("Error during loading: ", error);
            });
    }

    useEffect(() => {
        loadProject();
    }, []);

    return (
        <div>
            <h1>{project.name}</h1>
        </div>
  )
}