"use client";

import Link from 'next/link'
import Image from 'next/image' // Add this line
import React from 'react'

import { CustomButtonProps } from '@/types'
import { Sign } from 'crypto'
import CustomButton from "@/components/CustomButton"
import { useRouter } from 'next/navigation'



const About = () => {

  const router = useRouter()
  const isSignedIn = localStorage.getItem('isSignedIn') === 'true'; // Check local storage

  const navigateToSignIn = () => {
    router.push('/SignInPage')
  }
  return (
    <header className='w-full absolute z-10'>
      <nav className="max-w-[1440px] mx-auto flex justify-between 
      items-center sm:px-16 px-6 py-4">
        <Link href="/" className="flex justify-center items-center">
          <Image
              src="/Logo.webp" //or any logo picture we want
              alt="SBC"
              width={118}
              height={18}
              className="object-contain"
            />
        </Link>

        <CustomButton
          title={isSignedIn ? "Signed In" : "Sign in"}
          btnType="button"
          containerStyles="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded shadow-lg hover:shadow transition duration-200 ease-in-out"
          handleClick={navigateToSignIn}
        />

      </nav>
    </header>

  )        
      
}

export default About