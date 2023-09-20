import url from '../api.json'
import { useParams } from 'react-router-dom';
import { useState, useEffect } from 'react';
import TasksTable from '../components/TasksTable';

export default function ProjectPage() {
    const { project_id } = useParams();

    return (
        <div>
            <h1>{project_id}</h1>
        </div>
  )
}