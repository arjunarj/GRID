import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Line } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);
const nums1 = [11,4,22,55,6,23,56,43]
const nums2 = [43,56,2,56,6,2,11,34]
const options = {
  animation: {
    type: 'number',
    duration: 2000,
  },
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      position: 'top' ,
    },
    title: {
      display: true,
      text: 'Chart.js Line Chart',
    },
  },
};

const labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];


const data = {
  labels,
  datasets: [
    {
      label: 'Dataset 1',
      data: nums1,
      borderColor: 'rgb(255, 99, 132)',
      backgroundColor: 'rgba(255, 99, 132, 0.5)',
    },
    {
      label: 'Dataset 2',
      data: nums2,
      borderColor: 'rgb(53, 162, 235)',
      backgroundColor: 'rgba(53, 162, 235, 0.5)',
    },
  ],
};

export default function LineChart(){
  return <div style={{width: '600px',height: '400px'}}>
    <Line options={options} data={data}/>
  </div>
}