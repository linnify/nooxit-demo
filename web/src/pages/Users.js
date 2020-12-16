import React from 'react';
import {getUsers} from "../services/api";
import styled from "styled-components";
import ResourceItem from "../components/ResourceItem";
import ErrorMessage from "../components/ErrorMessage";
import {useApiResource} from "../hooks/api-resource";


const UsersList = styled.ul`
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
`

function Users() {
  const [users, error] = useApiResource(getUsers)
  const renderUsers = users.map((value, index) => <ResourceItem key={index} leftText={value.name} rightText={`${value.age} years`} />)
  
  return (
    <div>
      <h1>Users Page</h1>
      <div style={{ marginBottom: '18px'}}>Users page is accessible only for the users that belongs to the 'users' group </div>
      <ErrorMessage message={error}/>
      <UsersList>
        { renderUsers }
      </UsersList>
    </div>
  
  )
}

export default Users
