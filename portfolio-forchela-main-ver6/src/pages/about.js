import React, {useState} from 'react'
import  NavBar  from '../components/NavBar'
import  Sidebar  from '../components/SideBar'
import BannerHome from '../components/BannerHome'
import DivInfo from '../components/DivInfo'
import DivMeio from '../components/DivMeio'
import DivBaixo from '../components/DivBaixo'
import { home0bj0ne } from '../components/DivInfo/Data'
import Footer from '../components/Footer'
import Footer2 from '../components/Footer2'
import BannerAbout from '../components/BannerAbout'
import DivAbout from '../components/DivAbout'

const About = () => {
    const[isOpen, setIsOpen] = useState(false)

    const toggle = () => {
        setIsOpen(!isOpen);
    }

  return (
    <>
    <Sidebar isOpen={isOpen} toggle={toggle} />
    <NavBar toggle={toggle} /> 
    <BannerAbout />
    <DivAbout />
    <Footer />
    <Footer2 />
    </>
  )
}

export default About
