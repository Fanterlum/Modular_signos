// UserContext.js
import { createContext, useContext, useState } from 'react';

const JsonContext = createContext();

export const JsonProvider = ({ children }) => {
  const [Json, setJson] = useState(null);

  const clearJson = () => {
    setJson(null);
  };
  return (
    <JsonContext.Provider value={{ Json, setJson, clearJson}}>
      {children}
    </JsonContext.Provider>
  );
};

export const useJson = () => {
  return useContext(JsonContext);
};
