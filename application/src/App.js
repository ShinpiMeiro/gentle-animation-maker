import logo from './logo.svg';
import './App.css';
import { AppShell, Navbar, Header, Text, MediaQuery, Burger, ActionIcon, Group, Aside, Footer } from '@mantine/core';
import { MantineProvider, Button } from '@mantine/core';
import { SunIcon, MoonIcon } from '@modulz/radix-icons';
import { useState } from 'react';
import { createStyles, useMantineTheme } from '@mantine/styles';

import { MemoryRouter, NavLink, Route, Routes } from 'react-router-dom';

import Home from './Home';
import Settings from './Settings';

function App() {

  const views = [{
    path: '/',
    name: 'Home',
    exact: true,
    component: Home,
  }, {
    path: 'settings',
    name: 'Settings',
    component: Settings,
  },];

  const [opened, setOpened] = useState(false);
  const defaultColorScheme = 'dark';
  const [colorScheme, setColorScheme] = useState(defaultColorScheme);
  const toggleColorScheme = value => {
    const newValue = value || (colorScheme === 'dark' ? 'light' : 'dark');
    setColorScheme(newValue)
  };

  const useStyles = createStyles((theme) => ({
    navLink: {
      display: 'block',
      width: '100%',
      padding: theme.spacing.xs,
      borderRadius: theme.radius.md,
      color: colorScheme === 'dark' ? theme.colors.dark[0] : theme.black,
      textDecoration: 'none',
      '&:hover': {
        backgroundColor: colorScheme === 'dark' ? theme.colors.dark[6] : theme.colors.gray[1],
      }
    },
    navLinkActive: {
      backgroundColor: colorScheme === 'dark' ? theme.colors.dark[6] : theme.colors.gray[1],
      margin: '3%'
    },
  }));

  const { classes } = useStyles();

  return (
    <MantineProvider theme={{ colorScheme: colorScheme}} withGlobalStyles >
      <MemoryRouter>
        <AppShell fixed
          navbar={<Navbar p="xs" width={{ base: 200 }}>
              <Navbar.Section height={70} padding='xs'>
              
                <div style={{ display: 'flex', alignItems: 'center', height: '100%' }}>
                  <Text>神秘</Text>
                  <Text>Gentle animation maker</Text>
                  <div style= {{marginLeft: 'auto', }}>
                    <ActionIcon variant='default' onClick={() => toggleColorScheme()} size={30}>
                      {colorScheme === 'dark' ? <SunIcon /> : <MoonIcon />}
                    </ActionIcon>
                  </div>
                </div>
              </Navbar.Section>
              <Navbar.Section>
                {
                  views.map((view, index) =>
                    <NavLink align='left' to={view.path} key={index} onClick={() => setOpened(false)}
                    className={({ isActive }) => classes.navLink + ' ' + (isActive ? classes.navLinkActive : '')}>
                      <Group><Text>{view.name}</Text></Group>
                    </NavLink>
                  )
                }
              </Navbar.Section>  
          </Navbar>}
        >
        <Routes>
            {
            views.map((view, index) => <Route key={index} exact={view.exact} path={view.path} element={<view.component />} />)
            }
        </Routes>
        </AppShell>
      </MemoryRouter>
    </MantineProvider>
  );
}

export default App;
