import React from "react";
import Login from "../components/Login";
import {Route, Switch} from "react-router-dom";
import Nav from "../components/Nav";
import Members from "./Members";
import Users from "./Users";
import LoadingPage from "../components/LoadingPage";
import useAuth from "../hooks/auth";
import UserDetails from "../components/UserDetails";


function Home() {
  const [user, isLoading, logout] = useAuth()
  const isLoggedIn = !!user;
  
  const onLogout = () => {
    logout()
  }
  
  return (
    <div>
      { isLoading && <LoadingPage /> }
      
      { !isLoading && !isLoggedIn && <Login scopes={['email', 'profile', 'groups']}/>}
      
      { !isLoading && isLoggedIn && <div>
        <UserDetails user={user} logout={onLogout}/>
        
        <Nav/>
        
        <Switch>
          <Route path="/members">
            <Members isLoggedIn={isLoggedIn}/>
          </Route>
          <Route path="/">
            <Users isLoggedIn={isLoggedIn}/>
          </Route>
        </Switch>
      </div>
      }
    </div>
  )
}

export default Home
