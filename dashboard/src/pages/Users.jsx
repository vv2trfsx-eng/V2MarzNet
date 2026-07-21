import { useEffect, useState } from "react";
import api from "../api";


function Users(){

const [users,setUsers] = useState([]);


useEffect(()=>{

api.get("/users")
.then(response=>{

setUsers(
response.data.users
);

});


},[]);



return (

<div>

<h1>
👥 Users
</h1>


{

users.length === 0 ?

<p>
No users found
</p>

:

users.map((user,index)=>(

<p key={index}>
{user.username}
</p>

))

}


</div>

)

}


export default Users;
