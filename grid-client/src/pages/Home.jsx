import axios from "axios"
import { useState } from "react"
import LineChart from "../components/LineChart"

export default function Home(){
    const [player1,setPlayer1] = useState()
    const [player2,setPlayer2] = useState()
    const [players,setPlayers] = useState([])
    var [val,setval] = useState("")
    function handleChange(e){
        console.log(e.target.value)
        setval(e.target.value)
        axios.get(`http://localhost:8000/match?id=${val}`).then((res)=>{
        console.log(res.data)
        setPlayers(res.data)
       })
    }
    function handlePlayer1(e){
        setPlayer1(e.target.value)
        
    }
    function handlePlayer2(e){
        setPlayer2(e.target.value)
        
    }

    function handleSubmit(){
        console.log("called")
       console.log(player1)
       console.log(player2)
    }
    
    return <>
        <div>
            <p>Select a match:</p>
           
                <select value={val} onChange={handleChange}>
                    <option value="">--Select a match--</option>
                    <option value="1">forZe vs 9INE</option>
                </select>
            
            {players.length > 0 
            && <div>
                <div>
                <select value={player1} onChange={handlePlayer1}>
                <option value="">--Select Player 1--</option>
                <>{  
                    players.map((player)=>(
                        <option key={player}value={player}>{player}</option>
                    ))

                }</>
                </select>
                </div>
                <div>
                <select value={player2} onChange={handlePlayer2}>
                    <option value="">--Select Player 2--</option>
                {
                    players.map((player)=>(
                        <option key={player}value={player}>{player}</option>
                    ))

                }
                </select>
                </div>
                </div>
            }
            <input type="submit" onClick={handleSubmit}/>
            
        </div>
    </>
}