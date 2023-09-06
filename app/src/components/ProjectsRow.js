export default function ProjectsRow({project, removeProject}) {
    return (
        <tr>
            <td>{project.name}</td>
            <td>{project.owner}</td>
        </tr>
    )
}