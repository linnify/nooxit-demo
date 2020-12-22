import React from 'react';
import {getMembers} from "../services/api";
import styled from 'styled-components'
import ResourceItem from "../components/ResourceItem";
import ErrorMessage from "../components/ErrorMessage";
import {useApiResource} from "../hooks/api-resource";

const MemberList = styled.ul`
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
`

function Members({ user }) {
  const hasPermission = user.groups.includes("members")
  const [members, error] = useApiResource(getMembers, hasPermission)
  const renderMembers = members.map((value, index) => <ResourceItem key={index} leftText={value.team} rightText={value.role} />)
  
  return (
    <div>
      <h1>Members Page</h1>
      <div style={{ marginBottom: '18px'}}>Members page is accessible only for the users that belongs to the 'members' group </div>
  
      <ErrorMessage message={error}/>
      <MemberList>
        { renderMembers }
      </MemberList>
    </div>
  )
}

export default Members
