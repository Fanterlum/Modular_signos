// UserContext.js
import { createContext, useContext, useState } from 'react';

const ListContext = createContext();

export const PatientList = ({ children }) => {
  const [List, setList] = useState(null);

  const clearList = () => {
    setList(null);
  };
  return (
    <ListContext.Provider value={{ List, setList }}>
      {children}
    </ListContext.Provider>
  );
};

export const useList = () => {
  return useContext(ListContext);
};
