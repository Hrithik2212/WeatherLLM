import React from 'react'
import { Link } from 'react-router-dom'
import Header from '../../components/header/Header'
import Footer from '../../components/footer/Footer'
const Home = () => {
  return (
    <div className='md:pt-10'>
          
          <Header/>
          
        <div className='flex flex-col   my-font overflow-hidden'> 
          <div className='h-fit text-white   bg-[#003554]  p-[10px]   Staatliches '>
              <div className='mt-[150px] text-center flex flex-col w-full gap-3  md:p-10 justify-center items-center'>
                  
                      <h2 className='Staatliches text-[48px] font-bold max-md:text-[40px] '>Ready, Set, Chat!</h2>
                      <Link to="/chat" className='text-[18px] bg-black w-fit text-white p-2 rounded-lg my-font'>Chat Now</Link>
              </div>

              <Footer/>
          </div>
          



          
        </div>
    </div>
  )
}

export default Home;