import url from "../api.json";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Homepage() {
    const navigate = useNavigate();

    const [formData, setFormData] = useState({
        email: "",
        password: ""
    });

    const handleFormChange = (event) => {
        const { name, value } = event.target;
        setFormData((prevFormData) => ({
            ...prevFormData,
            [name]: value
        }));
    }

    const handleLogin = (event) => {
        event.preventDefault();
        fetch(url['url'] + `/users/login`, {
            method: 'POST', 
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(formData)
        })
            .then((response) => response.json())
            .then((data) => {
                localStorage.setItem('token', data.token);
                console.log("Login successful");
                console.log(localStorage.getItem('token'));
                navigate('/home')
            })
            .catch((error) => {
                console.error("Error during login:", error);
            });
    }

    return (
        <form onSubmit={handleLogin}>
            <h3>Login</h3>
            <input type="text" name="email" placeholder="Email" value={formData.email} onChange={handleFormChange} required />
            <br />
            <input type="text" name="password" placeholder="Password" value={formData.password} onChange={handleFormChange} required />
            <br />
            <button type="submit">Login</button>

        </form>
    )
}