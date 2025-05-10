import React from "react";

interface CommonButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  label: string;
}

export default function CommonButton({
  label,
  ...props
}: CommonButtonProps) {
  return <button {...props}>{label}</button>;
}
