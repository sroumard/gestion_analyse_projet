import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Bar } from 'react-chartjs-2';

function App() {
    const [kpis, setKpis] = useState([]);
    useEffect(() => {
        axios.get('http://localhost:8000/api/kpis/')
            .then(response => setKpis(response.data))
            .catch(error => console.error('Erreur : ', error));
    }, []);

    const data = {
        labels: kpis.map(kpi => kpi.nom),
        datasets: [
            {
                label: 'Valeurs des KPI',
                data: kpis.map(kpi => kpi.valeur),
                backgroundColor: 'rgba(75, 192, 192, 0.6)',
            },
        ],
    };

    return (
        <div>
            <h1>Tableau de Bord des KPI</h1>
            <Bar data={data} />
        </div>
    );
}

export default App;
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';

// Enregistrer les échelles et autres éléments nécessaires
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);