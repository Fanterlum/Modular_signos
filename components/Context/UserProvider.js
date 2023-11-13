import React, { createContext, useContext, useState } from 'react';

const UserContext = createContext();

export function UserProvider({ children }) {
  const [userID, setUserID] = useState(null);

  const clearUserID = () => {
    setUserID(null);
  };

  return (
    <UserContext.Provider value={{ userID, setUserID, clearUserID }}>
      {children}
    </UserContext.Provider>
  );
}

export function useUser() {
  return useContext(UserContext);
}
