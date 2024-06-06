import React from 'react'

const Footer = () => {
  return (
    <div className='mt-[100px] my-font text-center flex flex-col w-full gap-3  p-10  justify-center items-center bg-[#003554]'>
                      <div className='flex '>
                        <img alt='img-logo2' className='w-40' src="https://d23qowwaqkh3fj.cloudfront.net/wp-content/uploads/2022/01/srm-logo-white.svg.gzip"/>
                        <img alt='img-logo3' style={{"mixBlendMode":"screen"}} className='w-40' src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQocT5S9GtzMZYvJY1FBcMRa10wqXIylo3jbB_NA9yaB0nBBfjoDobqE_-TDfcBxEpInTA&usqp=CAU"/>
                      
                      </div>
                      <h2 className=' text-[16px] 2xl:text-[24px]  '>© 2023 All rights reserved.</h2>
                      <p className='my-font text-[16px] 2xl:text-[24px] max-w-[500px] opacity-[0.5]'>Created on Feb 29, 2024</p>
    </div>
  )
}

export default Footer