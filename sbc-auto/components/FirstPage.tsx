"use client";
import Image from 'next/image'
import CustomButton from './CustomButton'

export const FirstPage = () => {
//find a way to make these 3 lines of words appear in order with a delay
  return (
    <div className='first-page-background bg-black'>
        <div className="flex-1 pt-36 padding-x">
            <h1 className="Title__title flex justify-center items-center text-white text-3xl md:text-5xl font-bold mb-6">
                SBC Auto Solver
            </h1>
            <p className="flex justify-center items-center mb-8 text-xl md:text-2xl text-white">
                Solve any Squad Builder Challenges for EA FC 24 Ultimate Team
            </p>
            <p className="Title__description flex justify-center items-center mb-8 text-xl md:text-2xl text-white">
                To begin Solving Click Sign
            </p>

        </div>
        <div className='Title__image-container mx-auto max-w-4xl p-4'>
            <div className='Title__image rounded-lg overflow-hidden shadow-lg'>
                <Image src= "/SBC3.webp" alt="SBC" fill className="object-contain"/>
            </div>
        </div>
    </div>
  )
}

export default FirstPage
