import ProjectsRow from './ProjectsRow';

export default function ProjectsTable({projects, removeProject}) {
    return (
        <div>
            <table>
                <caption>My Projects</caption>
                <thead>
                    <tr>
                        <th>Trip</th>
                        <th>From</th>
                        <th>To</th>
                        <th>Organizer</th>
                    </tr>
                </thead>
                <tbody>
                    {projects.map((project, i) => <ProjectsRow project={project} removeProject={removeProject} key={i} />)}
                </tbody>
            </table>
        </div>
    )
}