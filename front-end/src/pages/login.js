import React from 'react'
import { useState } from 'react'
const Login = () => {
  const [page,setPage]=useState(true)
  const changePage =(e)=>{
    e.preventDefault()
    setPage(!page)
  }
  return (
    <div className='bg-[#003554] flex items-center justify-center h-screen '>
      
        <div className='bg-[#e8e6e6] max-md:min-w-[350px] min-w-[450px] flex flex-col  min-h-fit  w-[30%] rounded-3xl p-7'>
            
                <div className=' w-full flex items-center justify-center p-5'>
                    <h1 className='text-[25px]'>{page ?(<h1>Login</h1>):(<>SignUp</>)}</h1>
                </div>
                <div >
                    
                        {page ?(<form className='flex flex-col leading-[40px]  w-full h-full p-3'><label >Email</label>
                        <input type='email' placeholder='email...' className='shadow-2xl w-[90%] self-center rounded-md p-2 h-[50px]' required/>

                        <label>Password</label>
                        <input type='password' placeholder='password...' className='shadow-2xl w-[90%] self-center rounded-md p-2 h-[50px]' required/>
                        <button type='submit'  className='shadow-2xl w-[40%] text-[18px] bg-[#003554] text-white self-center rounded-md  mt-10 h-[40px] flex items-center justify-center p-2'>Submit</button>
                        <p className='self-center'>did't have account <button className='text-blue-700' onClick={changePage}>SignUp</button></p>
                        </form>)
                        :
                        (<form className='flex flex-col leading-[40px]  w-full h-full p-3'>
                          <label >Email</label>
                          <input type='email' placeholder='email...' className='shadow-2xl w-[90%] self-center rounded-md p-2 h-[50px]' required/>
                          
                          <label >Phone</label>
                          <input type='number' placeholder='number...' className='shadow-2xl w-[90%] self-center rounded-md p-2 h-[50px]' required/>

                          <label>Password</label>
                          <input type='password' placeholder='password...' className='shadow-2xl w-[90%] self-center rounded-md p-2 h-[50px]' required/>
                          <button type='submit'  className='shadow-2xl w-[40%] text-[18px] bg-[#003554] text-white self-center rounded-md  mt-10 h-[40px] flex items-center justify-center p-2'>Submit</button>
                          <p className='self-center'>have an account <button type='none' className='text-blue-700' onClick={changePage}>Login</button></p>
                        </form>)}
                    
                </div>
            
        </div>

    </div>
  )
}

export default Login