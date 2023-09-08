import { useNavigate } from 'react-router-dom';

export default function ProjectsRow({project, removeProject}) {
    let navigate = useNavigate();

    const handleProjectNavigate = () => {
        console.log(project.project_id)
        navigate(`/project/${project.project_id}`)
    }

    return (
        <tr onClick={handleProjectNavigate}>
            <td>{project.name}</td>
            <td>{project.owner}</td>
        </tr>
    )
}