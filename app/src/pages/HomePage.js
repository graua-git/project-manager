import url from '../api.json'
import { Link } from 'react-router-dom';
import { useState, useEffect } from 'react';
import ProjectsTable from '../components/ProjectsTable';

export default function Homepage() {
    const [user, setUser] = useState([]);
    const [greeting, setGreeting] = useState([]);
    const [projects, setProjects] = useState([]);
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
                loadProjects();
            })
            .catch((error) => {
                console.error("Error during loading: ", error);
            });
    }

    const loadProjects = async () => {
        fetch(url['url'] + `/projects/myprojects`, {
            method: 'GET',
            headers: {
                Authorization: `Bearer ${token}`
            }
        })
            .then((response) => response.json())
            .then((data) => {
                const projects = data;
                console.log(projects)
                setProjects(projects);
            })
            .catch((error) => {
                console.error("Error during loading: ", error);
            });
    }

    const handleCreateProject =  () => {
        navigate('/create-project', { replace: true });
    }

    const removeProject = () => {
        // ! Not Implemented
    }

    useEffect(() => {
        loadUser();
    }, []);

    return (
        <div>
            <h1>Project Manager</h1>
            <h2>Welcome{greeting}</h2>
            <button onClick={handleCreateProject}>Create Project</button>
            <ProjectsTable projects={projects} removeProject={removeProject}/>
        </div>
  )
}