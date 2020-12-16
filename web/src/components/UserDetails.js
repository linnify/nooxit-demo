import React from "react";
import styled from "styled-components";

const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 24px;
`

const Box = styled.div`
  border: 1px solid rgba(184,184,184,0.47);
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 16px;
`

const LogoutButton = styled.button`
  color: white;
  font-size: 16px;
  background-color: #f66e46;
  padding: 8px 16px;
  border-radius: 8px;
  outline: none;
  cursor: pointer;
  border: 0;
  margin-top: 18px;
`

function UserDetails({user, logout}) {
  
  const onLogout = () => logout()
  
  const emailVerified = user.email_verified ? 'Yes' : 'No'
  const groups = user.groups.join(", ")
  
  return (
    <Container>
      <Box>
        <div> {user.name} - { user.email }</div>
        <p> Email verified: { emailVerified }</p>
        <div> Groups: { groups }</div>
        <LogoutButton onClick={onLogout}> Logout </LogoutButton>
      </Box>
    </Container>
  )
}

export default UserDetails
