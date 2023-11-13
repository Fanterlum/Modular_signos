import { View, Text } from 'react-native'
import React from 'react'

const Users = () => {
    const Usuarios = [
        {
          id: 1,
          nombre: "Juan",
          apellidos: "Pérez",
          tipoUsuario: 1, // 1 para doctor, 2 para paciente, 3 para familiar
          fechaNacimiento: "1990-01-15",
          doctorACargo: null, // ID del doctor a cargo
          estadoActual: null, // 0, 1 o 2 (solo para pacientes)
          estadoFuturo: null, // 0, 1 o 2 (solo para pacientes)
          familiar: null, // ID del familiar (solo para familiares)
        },
        {
          id: 2,
          nombre: "María",
          apellidos: "González",
          tipoUsuario: 2,
          fechaNacimiento: "1985-05-20",
          doctorACargo: 1, // ID del doctor a cargo
          estadoActual: 1, // 0, 1 o 2 (solo para pacientes)
          estadoFuturo: 2, // 0, 1 o 2 (solo para pacientes)
          familiar: null,
        },
        {
          id: 3,
          nombre: "Ana",
          apellidos: "Martínez",
          tipoUsuario: 3,
          fechaNacimiento: "2000-09-10",
          doctorACargo: null,
          estadoActual: null,
          estadoFuturo: null,
          familiar: 2, // ID del paciente al que está relacionado (solo para familiares)
        },
        {
            id: 4,
            nombre: "Luis",
            apellidos: "García",
            tipoUsuario: 1,
            fechaNacimiento: "1982-03-12",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: null,
          },
          {
            id: 5,
            nombre: "Isabel",
            apellidos: "Rodríguez",
            tipoUsuario: 2,
            fechaNacimiento: "1995-07-25",
            doctorACargo: 1,
            estadoActual: 0,
            estadoFuturo: 1,
            familiar: null,
          },
          {
            id: 6,
            nombre: "Pedro",
            apellidos: "López",
            tipoUsuario: 3,
            fechaNacimiento: "2003-11-05",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: 5,
          },
          {
            id: 7,
            nombre: "Laura",
            apellidos: "Fernández",
            tipoUsuario: 1,
            fechaNacimiento: "1978-09-20",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: null,
          },
          {
            id: 8,
            nombre: "Carlos",
            apellidos: "Martín",
            tipoUsuario: 2,
            fechaNacimiento: "1989-04-18",
            doctorACargo: 1,
            estadoActual: 1,
            estadoFuturo: 2,
            familiar: null,
          },
          {
            id: 9,
            nombre: "Marta",
            apellidos: "Pérez",
            tipoUsuario: 3,
            fechaNacimiento: "2002-12-30",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: 5,
          },
          {
            id: 10,
            nombre: "Roberto",
            apellidos: "Gómez",
            tipoUsuario: 1,
            fechaNacimiento: "1985-06-14",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: null,
          },
          {
            id: 11,
            nombre: "Sofía",
            apellidos: "Hernández",
            tipoUsuario: 2,
            fechaNacimiento: "1993-08-28",
            doctorACargo: 1,
            estadoActual: 2,
            estadoFuturo: 0,
            familiar: null,
          },
          {
            id: 12,
            nombre: "Diego",
            apellidos: "Ramírez",
            tipoUsuario: 3,
            fechaNacimiento: "2001-02-10",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: 8,
          },
          {
            id: 13,
            nombre: "Natalia",
            apellidos: "López",
            tipoUsuario: 1,
            fechaNacimiento: "1976-11-03",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: null,
          },
          {
            id: 14,
            nombre: "Andrés",
            apellidos: "Fernández",
            tipoUsuario: 2,
            fechaNacimiento: "1998-05-09",
            doctorACargo: 1,
            estadoActual: 1,
            estadoFuturo: 1,
            familiar: null,
          },
          {
            id: 15,
            nombre: "Carmen",
            apellidos: "González",
            tipoUsuario: 3,
            fechaNacimiento: "2004-03-15",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: 11,
          },
          {
            id: 16,
            nombre: "Javier",
            apellidos: "Martínez",
            tipoUsuario: 1,
            fechaNacimiento: "1988-07-22",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: null,
          },
          {
            id: 17,
            nombre: "Lorena",
            apellidos: "Ortega",
            tipoUsuario: 2,
            fechaNacimiento: "1996-10-11",
            doctorACargo: 1,
            estadoActual: 0,
            estadoFuturo: 2,
            familiar: null,
          },
          {
            id: 18,
            nombre: "Alejandro",
            apellidos: "Sánchez",
            tipoUsuario: 3,
            fechaNacimiento: "2000-01-08",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: 14,
          },
          {
            id: 19,
            nombre: "Elena",
            apellidos: "Morales",
            tipoUsuario: 1,
            fechaNacimiento: "1983-04-19",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: null,
          },
          {
            id: 20,
            nombre: "Juan",
            apellidos: "Díaz",
            tipoUsuario: 2,
            fechaNacimiento: "1994-09-07",
            doctorACargo: 1,
            estadoActual: 2,
            estadoFuturo: 1,
            familiar: null,
          },
          {
            id: 21,
            nombre: "Raúl",
            apellidos: "Santos",
            tipoUsuario: 1,
            fechaNacimiento: "1977-12-01",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: null,
          },
          {
            id: 22,
            nombre: "Silvia",
            apellidos: "Ramírez",
            tipoUsuario: 2,
            fechaNacimiento: "1992-06-23",
            doctorACargo: 1,
            estadoActual: 1,
            estadoFuturo: 0,
            familiar: null,
          },
          {
            id: 23,
            nombre: "Pedro",
            apellidos: "Gómez",
            tipoUsuario: 3,
            fechaNacimiento: "2005-09-14",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: 19,
          },
          {
            id: 24,
            nombre: "Ana",
            apellidos: "López",
            tipoUsuario: 1,
            fechaNacimiento: "1984-03-08",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: null,
          },
          {
            id: 25,
            nombre: "José",
            apellidos: "Fernández",
            tipoUsuario: 2,
            fechaNacimiento: "1991-11-12",
            doctorACargo: 1,
            estadoActual: 2,
            estadoFuturo: 1,
            familiar: null,
          },
          {
            id: 26,
            nombre: "Isabel",
            apellidos: "Martínez",
            tipoUsuario: 3,
            fechaNacimiento: "2006-02-19",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: 21,
          },
          {
            id: 27,
            nombre: "Miguel",
            apellidos: "González",
            tipoUsuario: 1,
            fechaNacimiento: "1979-07-15",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: null,
          },
          {
            id: 28,
            nombre: "Laura",
            apellidos: "Hernández",
            tipoUsuario: 2,
            fechaNacimiento: "1997-05-04",
            doctorACargo: 1,
            estadoActual: 0,
            estadoFuturo: 1,
            familiar: null,
          },
          {
            id: 29,
            nombre: "Daniel",
            apellidos: "Sánchez",
            tipoUsuario: 3,
            fechaNacimiento: "2003-08-29",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: 25,
          },
          {
            id: 30,
            nombre: "Elena",
            apellidos: "Morales",
            tipoUsuario: 1,
            fechaNacimiento: "1988-01-10",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: null,
          },
          {
            id: 31,
            nombre: "Andrés",
            apellidos: "Díaz",
            tipoUsuario: 2,
            fechaNacimiento: "1993-04-17",
            doctorACargo: 1,
            estadoActual: 2,
            estadoFuturo: 0,
            familiar: null,
          },
          {
            id: 32,
            nombre: "María",
            apellidos: "Pérez",
            tipoUsuario: 3,
            fechaNacimiento: "2000-06-25",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: 28,
          },
          {
            id: 33,
            nombre: "Carlos",
            apellidos: "Gómez",
            tipoUsuario: 1,
            fechaNacimiento: "1986-11-05",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: null,
          },
          {
            id: 34,
            nombre: "Sofía",
            apellidos: "Ramírez",
            tipoUsuario: 2,
            fechaNacimiento: "1994-02-22",
            doctorACargo: 1,
            estadoActual: 1,
            estadoFuturo: 1,
            familiar: null,
          },
          {
            id: 35,
            nombre: "Juan",
            apellidos: "Santos",
            tipoUsuario: 3,
            fechaNacimiento: "2001-07-18",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: 32,
          },
          {
            id: 36,
            nombre: "Luis",
            apellidos: "Fernández",
            tipoUsuario: 1,
            fechaNacimiento: "1975-04-09",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: null,
          },
          {
            id: 37,
            nombre: "Carolina",
            apellidos: "Hernández",
            tipoUsuario: 2,
            fechaNacimiento: "1990-10-30",
            doctorACargo: 1,
            estadoActual: 0,
            estadoFuturo: 2,
            familiar: null,
          },
          {
            id: 38,
            nombre: "David",
            apellidos: "García",
            tipoUsuario: 3,
            fechaNacimiento: "2004-03-16",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: 34,
          },
          {
            id: 39,
            nombre: "Ana",
            apellidos: "Sánchez",
            tipoUsuario: 1,
            fechaNacimiento: "1989-08-12",
            doctorACargo: null,
            estadoActual: null,
            estadoFuturo: null,
            familiar: null,
          },
          {
            id: 40,
            nombre: "Roberto",
            apellidos: "Martínez",
            tipoUsuario: 2,
            fechaNacimiento: "1998-01-05",
            doctorACargo: 1,
            estadoActual: 2,
            estadoFuturo: 1,
            familiar: null,
          },
      ];
  return Usuarios;
}
export default Users