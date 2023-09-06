import ProjectsRow from './ProjectsRow';

export default function ProjectsTable({projects, removeProject}) {
    return (
        <div>
            <table>
                <caption>My Projects</caption>
                <thead>
                    <tr>
                        <th>Project</th>
                        <th>Creator</th>
                    </tr>
                </thead>
                <tbody>
                    {projects.map((project, i) => <ProjectsRow project={project} removeProject={removeProject} key={i} />)}
                </tbody>
            </table>
        </div>
    )
}