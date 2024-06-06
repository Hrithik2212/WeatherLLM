import React from 'react'
import ContentWrapper from '../contentWrapper/ContentWrapper'
const Nav = () => {
  return (
    <div className='my-font w-full fixed top-0 z-20 bg-white border-b  text-[#006494] text-[16px] p-5 px-10  max-md:p-5'>
        <ContentWrapper className="w-full mx-auto flex justify-between items-center">
            <div className='flex items-center justify-center gap-2'>
                <img alt='img-logo1' className='w-10' src="https://upload.wikimedia.org/wikipedia/en/f/fe/Srmseal.png"/>
                <h3 className='uppercase font-[700] text-[20px]'><a href='/'>Leave Bot</a></h3>
            </div>
            <div className='flex gap-5'>
                <a href='/contact' className='p-2'>Contact</a>
                <a href='/login' className='shadow-2xl  text-[18px] bg-[#003554] text-white  rounded-md p-2'>Login</a>
            </div>
        </ContentWrapper>
    </div>
  )
}

export default Nav