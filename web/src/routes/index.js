import React from 'react';
import { Route, Switch } from "react-router-dom";
import Members from "../pages/Members";
import Users from "../pages/Users";


export const HomeRoutes = ({user}) => {
  
  return (
    <Switch>
      <Route path="/members">
        <Members user={user}/>
      </Route>
      <Route path="/">
        <Users user={user} />
      </Route>
    </Switch>
  )
}
