import {useEffect,useState} from "react";
import api from "../api";


function Servers(){

const [servers,setServers]=useState([]);


useEffect(()=>{

api.get("/servers")
.then(res=>{

setServers(
res.data.servers
)

})

},[])



return (

<div>

<h1>
🌍 Servers
</h1>


{

servers.length===0 ?

<p>
No servers
</p>

:

servers.map((server,index)=>(

<p key={index}>
{server.name}
</p>

))

}


</div>

)

}


export default Servers;
