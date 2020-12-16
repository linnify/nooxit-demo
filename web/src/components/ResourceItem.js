import styled from "styled-components";
import React from "react";

const MemberItem = styled.div`
  display: flex;
  justify-content: space-between;
  padding: 12px;
  margin-bottom: 12px;
  border-bottom: 1px solid rgba(128,128,128,0.39);
  min-width: 250px;
`

function ResourceItem({ leftText, rightText}) {
  
  return (
    <MemberItem>
      <div> { leftText } </div>
      <div> { rightText } </div>
    </MemberItem>
  )
}

export default ResourceItem
