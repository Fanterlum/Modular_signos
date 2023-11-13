import React, { createContext, useContext, useState } from 'react';

const EmailContext = createContext();

export function EmailProvider({ children }) {
  const [Email, setEmail] = useState(null);

  const clearEmail = () => {
    setEmail(null);
  };

  return (
    <EmailContext.Provider value={{ Email, setEmail, clearEmail }}>
      {children}
    </EmailContext.Provider>
  );
}

export function useEmail() {
  return useContext(EmailContext);
}
