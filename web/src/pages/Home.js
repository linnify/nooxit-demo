import React from "react";
import Login from "../components/Login";
import Nav from "../components/Nav";
import LoadingPage from "../components/LoadingPage";
import useAuth from "../hooks/auth";
import UserDetails from "../components/UserDetails";
import {HomeRoutes} from "../routes";


function Home() {
  const [user, isLoading, logout] = useAuth()
  const onLogout = () => logout()
  
  return (
    <div>
      { isLoading && <LoadingPage /> }
      
      { !isLoading && !user && <Login scopes={['email', 'profile', 'groups']}/>}
      
      { !isLoading && user && <div>
        <UserDetails user={user} logout={onLogout}/>
        
        <Nav/>
        
        <HomeRoutes user={user} />
      </div>
      }
    </div>
  )
}

export default Home
